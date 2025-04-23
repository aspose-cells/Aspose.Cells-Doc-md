---
title: Configurando Márgenes
type: docs
weight: 20
url: /es/python-net/setting-margins/
description: En este artículo, aprenderás cómo establecer los márgenes de una hoja de cálculo de Excel usando código de ejemplo. También aprenderás cómo configurar programáticamente los márgenes para el centro de la página, los márgenes del encabezado y pie de página de la Configuración de página usando la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, establecer margen de hoja de Excel en Python, configurar márgenes del encabezado y pie de página en Python.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET admite completamente las opciones de configuración de página de Microsoft Excel. Los desarrolladores pueden necesitar configurar las opciones de configuración de página para las hojas de trabajo para controlar el proceso de impresión. Este tema explica cómo usar Aspose.Cells para Python via .NET para configurar los márgenes de la página.

{{% /alert %}}

## **Cómo Configurar Márgenes**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene la colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona la propiedad [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) utilizada para establecer las opciones de configuración de página de una hoja de cálculo. El atributo [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) es un objeto de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) que permite a los desarrolladores establecer diferentes opciones de diseño de página para una hoja de cálculo impresa. La clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) proporciona varias propiedades y métodos utilizados para establecer opciones de configuración de página.

## **Cómo Configurar Márgenes de Página**

Establezca los márgenes de página (izquierdo, derecho, arriba, abajo) utilizando los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). A continuación se enumeran algunos de los métodos que se utilizan para especificar los márgenes de página:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Cómo Centrar en la Página**

Es posible centrar algo en una página horizontal y verticalmente. Para ello, hay algunos miembros útiles de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) y [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Cómo Establecer Márgenes del Encabezado y Pie de Página**

Establezca los márgenes de encabezado y pie de página con los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) como [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) y [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
