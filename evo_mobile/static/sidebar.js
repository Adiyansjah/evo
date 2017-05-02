(function(){
  var sidebar = $('#sidebar');
  var toggleBtn = $('#toggle-btn');
  var menuBtn = $('#menu-btn');

  var toggleSidebar = function(){sidebar.toggle('slide');}
  
  toggleBtn.click(toggleSidebar);
  menuBtn.click(toggleSidebar);
})();