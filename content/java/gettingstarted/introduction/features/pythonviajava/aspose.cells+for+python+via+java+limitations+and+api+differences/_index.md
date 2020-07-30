---
title : "Aspose.Cells for Python via Java Limitations and API Differences" 
description : "" 
weight : 20031 
toc : false
type: docs
url: /java/gettingstarted/introduction/features/pythonviajava/aspose.cells+for+python+via+java+limitations+and+api+differences/
---

# Aspose.Cells for Java : Aspose.Cells for Python via Java Limitations and API Differences


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Public API Differences](#public-api-differences)
    *   1.1 [Example](#example)
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

