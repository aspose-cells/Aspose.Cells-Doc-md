---
title: Habilitar Propiedades Personalizadas de CSS al guardar en HTML
type: docs
weight: 320
url: /es/java/enable-css-custom-properties-while-saving-to-html/
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, para el escenario en que hay múltiples ocurrencias de una misma imagen en base64, con la propiedad personalizada, los datos de la imagen solo necesitan guardarse una vez para mejorar el rendimiento del HTML generado.Por favor usa la propiedad [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#EnableCssCustomProperties) y configúrala en **true** al guardar en HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Habilitar Propiedades Personalizadas de CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#EnableCssCustompPoperties). La captura muestra el efecto de esta propiedad cuando no está configurada en **true**. Por favor, descarga el [archivo Excel de ejemplo](50528260.xlsx) usado en este código y el [HTML generado](50528261.zip) como referencia.



## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-Java-HTML-·java" >}}
{{< app/cells/assistant language="java" >}}
