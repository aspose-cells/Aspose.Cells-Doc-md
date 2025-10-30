---
title: Actualizar automáticamente el objeto OLE mediante Microsoft Excel con Golang vía C++
linktitle: Actualizar automáticamente el objeto OLE
type: docs
weight: 270
url: /es/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aprender cómo actualizar automáticamente los objetos OLE en Microsoft Excel usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la propiedad [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) para actualizar el objeto OLE cuando se abre el archivo de Excel en Microsoft Excel. Debido a esta propiedad, el objeto OLE mostrará la imagen OLE correcta generada por Microsoft Excel.

{{% /alert %}}

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](5115231.xlsx) que tiene una imagen OLE no real. El objeto OLE es en realidad un documento de Microsoft Word, pero el archivo de Excel de muestra muestra la imagen del animal en lugar de la imagen de Microsoft Word. Sin embargo, si abres el [archivo de Excel de salida](5115225.xlsx), verás que Microsoft Excel muestra la imagen OLE correcta.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
