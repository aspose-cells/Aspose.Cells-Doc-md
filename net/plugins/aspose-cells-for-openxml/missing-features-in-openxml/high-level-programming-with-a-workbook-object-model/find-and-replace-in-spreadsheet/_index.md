---
title: Find and Replace in Spreadsheet
type: docs
weight: 30
url: /net/find-and-replace-in-spreadsheet/
---

![todo:image_alt_text](/download/thumbnails/5020491/1646666428)

When we click on find button following is the code:

{{< highlight csharp >}}

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

Clicking on Replace button following code is executed:

{{< highlight csharp >}}

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
## **Download Sample Code**
- [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Find%20and%20replace%20%28Aspose.Cells%29.zip)