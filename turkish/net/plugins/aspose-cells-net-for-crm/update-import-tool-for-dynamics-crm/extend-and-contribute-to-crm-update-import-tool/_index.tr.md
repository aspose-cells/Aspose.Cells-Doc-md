---
title: Genişletin ve CRM Güncelleme İçe Aktarma Aracına Katkıda Bulunun
type: docs
weight: 10
url: /tr/net/extend-and-contribute-to-crm-update-import-tool/
---
En son kaynak kodunu şu adresten indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Dynamics%20CRM/Aspose.Plugins.UpdateImportTool).

Verileri CRM'den Excel'e Aktarma

{{< highlight "cs" >}}

  SaveFileDialog fileDialog = new SaveFileDialog();

 fileDialog.DefaultExt = ".xlsx";

 fileDialog.FileName = "Aspose ImportTool Export.xlsx";

 if (fileDialog.ShowDialog().Value)

 {

    string FileName = fileDialog.FileName;

    Workbook workbook = new Workbook();

    workbook.Worksheets.Add("Aspose Export");

    Worksheet MyWorksheet = workbook.Worksheets["Aspose Export"];

    int i = 0;

    foreach (string attrib in SelectedAttributes)

    MyWorksheet.Cells[0, i++].Value = attrib;

    int Row = 1,cell=0;

    foreach (Entity record in Result.Entities)

    {

       cell = 0;

       foreach (string attribute in SelectedAttributes)

       {

          if (record.Contains(attribute))

          {

             MyWorksheet.Cells[Row,cell].Value = record[attribute].ToString();

          }

          cell++;

       }

       Row++;

     }

     workbook.Save(FileName, SaveFormat.Xlsx);

}


{{< /highlight >}}

Verileri Excel'den CRM'ye Aktarın

{{< highlight "cs" >}}

  if (ctrl.CrmConnectionMgr != null && ctrl.CrmConnectionMgr.CrmSvc != null && ctrl.CrmConnectionMgr.CrmSvc.IsReady)

 {

    CrmServiceClient svcClient = ctrl.CrmConnectionMgr.CrmSvc;

    if (svcClient.IsReady)

    {

        OpenFileDialog fileDialog = new OpenFileDialog();

        fileDialog.DefaultExt = ".xlsx";

        if (fileDialog.ShowDialog().Value)

        {

           string FileName = fileDialog.FileName;

           Workbook workbook = new Workbook(FileName);

           Worksheet MyWorksheet = workbook.Worksheets["Aspose Export"];

           DataTable dt = MyWorksheet.Cells.ExportDataTable(0, 0, MyWorksheet.Cells.Rows.Count, MyWorksheet.Cells.Columns.Count, true);

           foreach (DataRow dr in dt.Rows)

           {

               Entity CrmRecord = new Entity(SelectedEntity);

               foreach (DataColumn th in dt.Columns)

               {

                  CrmRecord.Attributes.Add(th.ColumnName, dr[th.ColumnName].ToString());

               }

               CreateRequest req = new CreateRequest();

               req.Target = CrmRecord;

               CreateResponse res = (CreateResponse)svcClient.OrganizationServiceProxy.Execute(req);

            }

        }

    }

 }


{{< /highlight >}}
