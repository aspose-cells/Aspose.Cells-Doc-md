---
title: Begränsningar och API avvikelser
type: docs
weight: 10
url: /sv/python-java/limitations-and-api-differences/
keywords: "python, excel, begränsning, api, skillnader"
description: "Aspose.Cells för Python via Java begränsningar och api skillnader."
---

## **Offentliga API-avvikelser**
### **Exempel**
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

