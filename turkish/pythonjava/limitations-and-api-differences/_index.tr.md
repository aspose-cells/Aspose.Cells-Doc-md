---
title: Sınırlamalar ve API Farklılıkları
type: docs
weight: 10
url: /tr/python-java/limitations-and-api-differences/
keywords: "python, excel, sınırlama, api, farklılıklar"
description: "Aspose.Cells for Python via Java sınırlamaları ve api farklılıkları."
---

## **Genel API Farklılıkları**
### **Örnek**
**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

public class Test1 {

	public static void main(String[] args) throws Exception {

		Workbook workbook = new Workbook(FileFormatType.XLSX);

		workbook.getWorksheets().get(0).getCells().get("A1").putValue("testing...");

		workbook.save("wb.xlsx");

	}

}

{{< /highlight >}}



**Aspose.Cells for Python via Java**

{{< highlight python >}}

 import jpype

import asposecells


def run():

    kwargs = dict(convertStrings=True)

    jpype.startJVM(**kwargs)

    from asposecells.api import Workbook, CellsHelper, FileFormatType, License

    workbook = Workbook(FileFormatType.XLSX)

    workbook .getWorksheets().get(0).getCells().get("A1").putValue("testing...")

    workbook .save("wb.xlsx")

    jpype.shutdownJVM()

{{< /highlight >}}

