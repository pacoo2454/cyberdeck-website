/*
 * updates-renderer.js
 * Shared rendering utilities for displaying CYBERDECK_UPDATES entries.
 * Exposes window.CyberDeckRenderer for use by page-specific scripts.
 */
(function () {
  var TAG_CLASSES = {
    'release':      'tag--release',
    'fix':          'tag--fix',
    'announcement': 'tag--announcement'
  };

  function escapeHTML(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function tagClass(tag) {
    return TAG_CLASSES[tag.toLowerCase()] || 'tag--announcement';
  }

  function formatDate(dateStr) {
    return new Date(dateStr + 'T00:00:00').toLocaleDateString('en-US', {
      year: 'numeric', month: 'long', day: 'numeric'
    });
  }

  /* Converts **bold**, *italic* within a single line of text */
  function inlineMarkdown(str) {
    str = str.replace(/\*\*([^*\n]+)\*\*/g, '<strong>$1</strong>');
    str = str.replace(/\*([^*\n]+)\*/g,     '<em>$1</em>');
    return str;
  }

  /*
   * Converts a body string (with \n line breaks and \n\n paragraph
   * breaks) into HTML. Blocks starting with "- " become <ul> lists;
   * everything else becomes a <p> with <br> for single line breaks.
   */
  function parseMarkdown(text) {
    text = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
    var blocks = text.trim().split(/\n{2,}/);
    return blocks.map(function (block) {
      block = block.trim();
      if (!block) return '';
      var lines = block.split('\n');
      var isList = lines.every(function (l) { return /^[-*]\s/.test(l); });
      if (isList) {
        return '<ul>' + lines.map(function (l) {
          return '<li>' + inlineMarkdown(l.replace(/^[-*]\s+/, '')) + '</li>';
        }).join('') + '</ul>';
      }
      return '<p>' + inlineMarkdown(lines.join('<br>')) + '</p>';
    }).join('');
  }

  window.CyberDeckRenderer = {
    tagClass:      tagClass,
    escapeHTML:    escapeHTML,
    formatDate:    formatDate,
    inlineMarkdown: inlineMarkdown,
    parseMarkdown:  parseMarkdown
  };
})();
