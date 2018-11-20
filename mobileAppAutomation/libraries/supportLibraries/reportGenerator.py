import json
import os

style='''<style>
.execution_table {
  margin: 1em 0;
  width: 100%;
  overflow: hidden;
  background: #FFF;
  color: #2d3f5b;
  border-radius: 10px;
  border: 1px solid #002200;
  border-collapse: collapse;
}
.execution_table tr {
  border: 1px solid #002200;
}
.execution_table tr:nth-child(odd) {
  background-color: #EAF3F3;
}
.execution_table th {
  border: 1px solid #002200;
  background-color: #2d3f5b;
  color: #FFF;
}
.execution_table td {

  border: 1px solid #002200;
}
.execution_table td:nth-child(6) {
  word-break:break-all;
  border: 1px solid #002200;
}
.execution_table th, .execution_table td {
  text-align: left;
  margin: .5em 1em;
  display: table-cell;
  padding: 0.5em;
}

.summary_table {
  margin: 1em 0;
  width: 45%;
  overflow: hidden;
  background: #FFF;
  color: #024457;
  border-radius: 10px;
  border: 1px solid #002200;
  border-collapse: collapse;
}
.summary_table tr {
  border: 1px solid #002200;
  padding: 1em;
}
.summary_table tr:nth-child(odd) {
  background-color: #EAF3F3;
}
.summary_table td:first-child{
  font-weight:bold;
}
.summary_table th {
  border: 1px solid #002200;
  background-color: #2d3f5b;
  color: #FFF;

  padding: 0.7em;
  text-align: left;
}
.summary_table td {
  word-wrap: break-word;
  max-width: 28.9em;
  padding: 0.5em;
  border: 1px solid #002200;
}
body {
  padding: 0 2em;
  font-family: Arial, sans-serif;
  color: #024457;
  background: #f2f2f2;
}
h1 {
  font-family: Verdana;
  font-weight: normal;
  color: #024457;
}
</style>'''

elements = ['''<h1><center><b>Execution Results</b></center></h1>''']

table_column1 = '''  <tr>
    <th>TestCase Name</th>
    <th>Start-Time</th>
    <th>End-Time</th>
    <th>Duration</th>
    <th>Status</th>
    <th>Message</th>
    <th>Screenshot</th>
  </tr>'''


def form_tr(elem):
    tr_start = '<tr>'
    tr_end = '</tr>'
    return tr_start + elem + tr_end

def form_td(elem):
    td_start = '<td>'
    td_end = '</td>'
    return td_start + str(elem) + td_end

def form_a(path,value):
    a_start = '<a href="{}" style="text-decoration:none;">'.format(path)
    a_end = '</a>'
    return a_start + value + a_end

def form_img(path):
    a_start = '<img src="{}" alt="" border=3 height=100 width=100">'.format(path)
    a_end = '</img>'
    return a_start + a_end

def form_run_summary_table(rows):
    table_start = '<table class="execution_table">'
    table_end = '</table>'
    trs=''
    for i in rows:
        data = rows[i]
        if data["screenshot"]:
            data_screenshot = form_a(data["screenshot"],form_img(data["screenshot"]))
        else:
            data_screenshot = ''

        tds = ''
        dict_ids = [i,data["start"],data["end"],data["duration"],data["result"],data["message"],data_screenshot]
        for ids in dict_ids:
            tds = tds + form_td(ids)
        trs = trs + form_tr(tds)
    return table_start + table_column1 + trs + table_end

def generateJSONReport(report_path,data):
    try:
        with open(report_path, 'wb') as out:
            json.dump(data, out, separators=(',', ':'), indent=4)

        return True
    except Exception as exp:
        print "Error generating JSON report!: {}".format(exp)
        return False

def generateReportHTML(report_path,data):
    try:
        elements.append(form_run_summary_table(data))
        elements.append('<br>')
        html_file = open(report_path,'wb')
        html = '<html><div align="center">'
        html = html + ''.join(elements)+'</div></html>'
        html_file.write(style + html)
        html_file.close()
        return True
    except Exception as exp:
        print "Error Generating HTML Report! {0}".format(exp)
        return False