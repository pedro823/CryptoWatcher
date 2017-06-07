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

function create_chart_canvasJS(object) {
  var chart = new CanvasJS.Chart("chart", {
    zoomEnabled : true,
    legend: {
        cursor: "pointer",
        itemclick: function (e) {
            if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                e.dataSeries.visible = false;
            } else {
                e.dataSeries.visible = true;
            }
            e.chart.render();
        }
    },
    title: { text: "CryptoWatcher" },
    axisY: { includeZero : false, prefix: "R$" },
    data: object,
  });
  chart.render();
}

$(document).ready(function() {
  var a = load_json("http://localhost:8000/history.json");
  create_chart_canvasJS(a);
});
