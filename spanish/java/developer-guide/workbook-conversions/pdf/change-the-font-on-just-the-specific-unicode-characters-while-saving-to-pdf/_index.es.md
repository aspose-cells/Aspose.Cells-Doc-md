---
title: Cambiar la fuente solo de los caracteres Unicode específicos al guardar en PDF
type: docs
weight: 150
url: /es/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Algunos caracteres Unicode no se pueden mostrar con la fuente especificada por el usuario. Uno de estos caracteres Unicode es **Guión no separable** (U+2011) y su número Unicode es 8209. Este carácter no se puede mostrar con **Times New Roman**, pero se puede mostrar con otras fuentes como **Arial Unicode MS**.

Cuando dicho carácter ocurre dentro de alguna palabra u oración que está en una fuente específica como Times New Roman, entonces Aspose.Cells cambia la fuente de toda la palabra o oración a la fuente que podría mostrar este carácter como Arial Unicode MS.

Sin embargo, este comportamiento es indeseable para algunos usuarios y quieren que solo se cambie la fuente del carácter específico en lugar de cambiar la fuente de toda la palabra u oración.

Para resolver este problema, Aspose.Cells proporciona la propiedad [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) que debe establecerse como **true** para que solo se cambie la fuente del carácter específico que no se puede mostrar y la fuente para el resto de la palabra u oración permanezca igual.

{{% /alert %}}

## **Ejemplo**

La siguiente captura de pantalla compara los dos PDF de salida generados por el código de ejemplo a continuación. Uno se generó sin establecer la propiedad [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) y el otro se generó después de establecer la propiedad [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) en **true**. Como puede ver en el primer PDF, la fuente de toda la oración ha cambiado de Times New Roman a Arial Unicode MS debido al Guión no separable. Mientras que en el segundo PDF, solo la fuente del Guión no separable ha cambiado.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
{{< app/cells/assistant language="java" >}}
