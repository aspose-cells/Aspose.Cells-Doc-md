---
title: Actualizar días conservando el historial de registros de revisión en un libro compartido
type: docs
weight: 80
url: /es/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Escenarios de uso posibles**

Cuando compartes un libro, aparece una opción que dice ***Mantener el historial de cambios durante N días*** como se muestra en la siguiente captura de pantalla. Puedes actualizar el número de días para conservar el historial usando Aspose.Cells para Python via .NET con la propiedad [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar Días de Conservación del Historial de Revisiones en Libro de Trabajo Compartido**

El siguiente código de muestra crea un libro de trabajo vacío, luego lo comparte y actualiza los días de registro de revisión para preservar el historial a 7 días, que normalmente son 30 días. Consulte el [archivo Excel de salida](60489773.xlsx) generado por el código como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
