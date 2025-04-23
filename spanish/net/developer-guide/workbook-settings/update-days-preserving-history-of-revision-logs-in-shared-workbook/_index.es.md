---
title: Actualizar días conservando el historial de registros de revisión en un libro compartido
type: docs
weight: 80
url: /es/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Escenarios de uso posibles**

Cuando comparte un libro de trabajo, obtiene una opción que dice ***Mantener el historial de cambios durante N días*** como se muestra en la siguiente captura de pantalla. Puede actualizar el número de días para preservar el historial usando Aspose.Cells con la propiedad [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/net/aspose.cells.revisions/revisionlogcollection/properties/dayspreservinghistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar Días de Conservación del Historial de Revisiones en Libro de Trabajo Compartido**

El siguiente código de muestra crea un libro de trabajo vacío, luego lo comparte y actualiza los días de registro de revisión para preservar el historial a 7 días, que normalmente son 30 días. Consulte el [archivo Excel de salida](60489773.xlsx) generado por el código como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
