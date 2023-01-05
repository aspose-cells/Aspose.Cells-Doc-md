---
title: Elektronik Tabloda Bul ve Değiştir
type: docs
weight: 30
url: /tr/net/find-and-replace-in-spreadsheet/
---
![yapılacaklar:resim_alternatif_metin](Find_and_Replace.png)

Bul butonuna tıkladığımızda aşağıdaki kod:

{{< highlight "csharp" >}}

 if (TXBX_Find.Text != "")

{

	 workbook = new Workbook(FOD_OpenFile.FileName);

	FindOptions Opts = new FindOptions();

	Opts.LookInType = LookInType.Values;

	Opts.LookAtType = LookAtType.Contains;

	string found = "";

	Cell cell = null;

	foreach (Worksheet sheet in workbook.Worksheets)

	{

		found += Environment.NewLine + "Sheet: " + sheet.Name + ":";

		do

		{

			cell = sheet.Cells.Find(TXBX_Find.Text, cell, Opts);

			if (cell != null)

				found += cell.Name + ",";

		}

		while (cell != null);

	}

	LBL_FindResults.Text = found;

}

{{< /highlight >}}

Değiştir düğmesine tıklandığında aşağıdaki kod yürütülür:

{{< highlight "csharp" >}}

 if (TXBX_Find.Text != "" && TXBX_Replace.Text!="")

{

	workbook = new Workbook(FOD_OpenFile.FileName);

	FindOptions Opts = new FindOptions();

	Opts.LookInType = LookInType.Values;

	Opts.LookAtType = LookAtType.Contains;

	string found = "";

	Cell cell = null;

	foreach (Worksheet sheet in workbook.Worksheets)

	{

		do

		{

			cell = sheet.Cells.Find(TXBX_Find.Text, cell, Opts);

			if (cell != null)

			{

				string celltext = cell.Value.ToString();

				celltext = celltext.Replace(TXBX_Find.Text, TXBX_Replace.Text);

				cell.PutValue(celltext);

			}

		}

		while (cell != null);

	}

	LBL_FindResults.Text = "Replaced All Existing Values, Save the file now";

}

{{< /highlight >}}

## **Örnek Kodu İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Find%20and%20replace%20%28Aspose.Cells%29.zip)
