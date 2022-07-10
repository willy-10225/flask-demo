const mainE1=document.querySelector('#main');

$(document).ready(()=>{
    drawPM25();
});


function drawPM25(){
    $.ajax(
        {
            url:"/pm25-json",
            type:"POST",
            dataType:"json",
            success:(data)=>{
                console.log(data);
                // 基于准备好的dom，初始化echarts实例
                let myChart = echarts.init(mainE1);

                // 指定图表的配置项和数据
                let option = {
                title: {
                    text: 'PM2.5數據圖'
                },
                tooltip: {},
                legend: {
                    data: ['站點']
                },
                xAxis: {
                    data: data['stationname']
                },
                yAxis: {},
                series: [
                    {
                    name: 'PM2.5',
                    type: 'bar',
                    data: data['result']
                    }
                ]
                };

                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
            },
            error: ()=>{
                alert("error!");
            }
        }
    )
}
