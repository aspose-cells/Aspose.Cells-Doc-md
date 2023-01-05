---
title: 限制和 API 差异
type: docs
weight: 10
url: /zh/python-java/limitations-and-api-differences/
keywords: python, excel, limitation, api, difference
description: Aspose.Cells for Python via Java 限制和api差异
---
## **公共 API 差异**
### **例子**
**Aspose.Cells for Java**

{{< highlight "java" >}}

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

{{< highlight "python" >}}

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

