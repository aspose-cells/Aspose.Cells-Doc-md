---
title: Aspose.Cells ile Birleştirilmiş Hücreleri Algıla
type: docs
weight: 30
url: /tr/java/detect-merged-cells-using-aspose-cells/
---

## **Aspose.Cells - Birleştirilmiş Hücreleri Belirleme**
Microsoft Excel'de birkaç hücre birleştirilebilir. Bu genellikle karmaşık tablolar oluşturmak veya birkaç sütunu kapsayan bir başlık oluşturmak için kullanılır.
Aspose.Cells, bir çalışma sayfasındaki birleştirilmiş hücre alanlarını tanımlamanıza olanak tanır. Onları tekrar birleştirebilirsiniz.

**Java**

{{< highlight java >}}

 //Get the merged cells list to put it into the arraylist object

ArrayList<CellArea> al = worksheet.getCells().getMergedCells();

//Define cellarea

CellArea ca;

//Define some variables

int frow, fcol, erow, ecol;

// Print Message

System.out.println("Merged Areas: \n"+ al.toString());

//Loop through the arraylist and get each cellarea to unmerge it

for(int i = al.size()-1 ; i > -1; i--)

{

	ca = new CellArea();

	ca = (CellArea)al.get(i);

	frow = ca.StartRow;

	fcol = ca.StartColumn;

	erow = ca.EndRow;

	ecol = ca.EndColumn;

	System.out.println((i+1) + ". [" + fcol +"," + frow +"] " + "[" + ecol +"," + erow +"]");

	worksheet.getCells().unMerge(frow, fcol, erow, ecol);

}

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Tabloda Birleştirilmiş Hücreleri Bul](/cells/tr/java/detect-merged-cells-in-a-worksheet)'i ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
