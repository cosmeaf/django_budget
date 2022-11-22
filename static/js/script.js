/*----------------------------------------------------------------------
# All Scrips here will extends to all pages
-----------------------------------------------------------------------*/

// 1) Script to auto hide the bootstrap alert after 3 seconds
$(document).ready(function () {
  setTimeout(function () {
    $('.alert').alert('close');
  }, 3000);
});
