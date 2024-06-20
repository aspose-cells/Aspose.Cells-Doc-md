---
title: Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino
type: docs
weight: 10
url: /es/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **Escenarios de uso posibles**

Cuando agregas una nueva hoja a un libro de trabajo, esta contiene las configuraciones de la Configuración de Página predeterminadas. Puede haber momentos en los que necesites transferir las configuraciones ([**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)) desde una hoja de cálculo a otra. Este documento explica cómo copiar las configuraciones de la Configuración de Página de una hoja a otra utilizando las APIs de Aspose.Cells.

## **Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino**

El siguiente código de muestra ilustra cómo copiar las configuraciones de la configuración de página desde una hoja de cálculo a otra utilizando el método [**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions)). Por favor, consulta el código de muestra y su salida en consola para referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
