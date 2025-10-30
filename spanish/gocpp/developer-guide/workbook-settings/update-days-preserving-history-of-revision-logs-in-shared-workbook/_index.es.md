---
title: Actualizar los días preservando el historial de registros de revisiones en un libro de trabajo compartido con Golang vía C++
linktitle: Actualizar días conservando el historial de registros de revisión en un libro compartido
type: docs
weight: 80
url: /es/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Aprender cómo actualizar el número de días para preservar el historial en un libro de trabajo compartido usando Aspose.Cells con Golang vía C++
---

## **Escenarios de uso posibles**

Cuando comparte un libro de trabajo, obtiene una opción que dice ***Mantener el historial de cambios durante N días*** como se muestra en la siguiente captura de pantalla. Puede actualizar el número de días para preservar el historial usando Aspose.Cells con la propiedad [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar Días de Conservación del Historial de Revisiones en Libro de Trabajo Compartido**

El siguiente código de muestra crea un libro de trabajo vacío, luego lo comparte y actualiza los días de registro de revisión para preservar el historial a 7 días, que normalmente son 30 días. Consulte el [archivo Excel de salida](60489773.xlsx) generado por el código como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
