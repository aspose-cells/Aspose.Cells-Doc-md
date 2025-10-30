---
title: Habilitar propiedades personalizadas de CSS al guardar en HTML con Golang vía C++
linktitle: Habilitar Propiedades Personalizadas de CSS al guardar en HTML
type: docs
weight: 320
url: /es/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: Aprende cómo habilitar las propiedades personalizadas de CSS al guardar archivos de Excel en HTML usando Aspose.Cells for C++. Mejora el rendimiento reduciendo datos de imagen redundantes.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, en el escenario que haya múltiples ocurrencias para una misma imagen en base64, con propiedad personalizada, solo es necesario guardar los datos de la imagen una vez, mejorando así el rendimiento del HTML resultante. Usa la propiedad [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/) y configúrala a **true** al guardar en HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Habilitar Propiedades Personalizadas de CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/). La captura de pantalla muestra el efecto de esta propiedad cuando no está configurada a **true**. Por favor, descarga el [archivo de Excel de ejemplo](50528260.xlsx) utilizado en este código y el [HTML de salida](50528261.zip) generado para referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}
