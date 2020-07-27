+++
title = "Aspose.Cells for Python via Java Limitations and API Differences" 
description = "" 
weight = 20031 
+++

Aspose.Cells for Java : Aspose.Cells for Python via Java Limitations and API Differences  

# Aspose.Cells for Java : Aspose.Cells for Python via Java Limitations and API Differences


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Public API Differences](#Aspose.CellsforPythonviaJavaLimitationsandAPIDifferences-PublicAPIDifferences)
    *   1.1 [Example](#Aspose.CellsforPythonviaJavaLimitationsandAPIDifferences-Example)
{{< /panel >}}
 

## Public API Differences

### Example

**Aspose.Cells for Java**

{{< code lang="cs" >}}
import com.aspose.cells.*;

public class Test1 {
	public static void main(String[] args) throws Exception {
		Workbook workbook = new Workbook(FileFormatType.XLSX);
		workbook.getWorksheets().get(0).getCells().get("A1").putValue("testing...");
		workbook.save("wb.xlsx");
	}
}
{{< /code >}}

**Aspose.Cells for Python via Java**

import jpypeimport asposecellsdef run():    kwargs = dict(convertStrings=True)    jpype.startJVM(\*\*kwargs)    from asposecells.api import Workbook, CellsHelper, FileFormatType, License    workbook = Workbook(FileFormatType.XLSX)    workbook .getWorksheets().get(0).getCells().get("A1").putValue("testing...")    workbook .save("wb.xlsx")    jpype.shutdownJVM()

