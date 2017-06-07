function load_json(file_name) {
  var json_archive = (function() {
    var json = null;
    $.ajax({
      'async' : false,
      'global' : false,
      'url' : file_name,
      'dataType' : "json",
      'success' : function(data) {
        json = data;
      }
    });
    return json;
  })();
  return json_archive;
}

function create_chart(object) {
  var data_array = [];
  var symbol_array = [];
  for(var i = 0; i < object.length; i++) {
  }
  console.log(object)
  var chart = new CanvasJS.Chart("chart", {
    title: { text: "CryptoWatcher" },
    axisY: { includeZero : false },
    data: [

    ],
  });
  chart.render();
}

$(document).ready(function() {
  var a = load_json("http://localhost:8000/history.json");
  create_chart(a);
});
