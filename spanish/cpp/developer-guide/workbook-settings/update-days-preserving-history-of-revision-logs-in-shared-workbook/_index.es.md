---
title: Actualizar días preservando el historial de registros de revisión en un libro compartido con C++
linktitle: Actualizar días conservando el historial de registros de revisión en un libro compartido
type: docs
weight: 80
url: /es/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Aprende cómo actualizar el número de días para preservar el historial en un libro compartido usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Cuando comparte un libro de trabajo, obtiene una opción que dice ***Mantener el historial de cambios durante N días*** como se muestra en la siguiente captura de pantalla. Puede actualizar el número de días para preservar el historial usando Aspose.Cells con la propiedad [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar Días de Conservación del Historial de Revisiones en Libro de Trabajo Compartido**

El siguiente código de muestra crea un libro de trabajo vacío, luego lo comparte y actualiza los días de registro de revisión para preservar el historial a 7 días, que normalmente son 30 días. Consulte el [archivo Excel de salida](60489773.xlsx) generado por el código como referencia.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
