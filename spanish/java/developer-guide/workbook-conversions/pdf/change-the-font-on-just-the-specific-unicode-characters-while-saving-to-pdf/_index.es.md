---
title: Cambie la fuente solo en los caracteres Unicode específicos mientras guarda en PDF
type: docs
weight: 150
url: /es/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Algunos caracteres Unicode no se pueden mostrar con la fuente especificada por el usuario. Uno de esos caracteres Unicode es**Guión de no separación** (U+2011) y su número Unicode es 8209. Este carácter no se puede mostrar con**Times New Roman** , pero se puede mostrar con otras fuentes como**Arial Unicode MS**.

Cuando un carácter de este tipo aparece dentro de una palabra u oración que está en una fuente específica como Times New Roman, entonces Aspose.Cells cambia la fuente de la palabra u oración completa a una fuente que podría mostrar este carácter como Arial Unicode a MS.

Sin embargo, este es un comportamiento indeseable para algunos usuarios y solo quieren que se cambie la fuente del carácter específico en lugar de cambiar la fuente de la palabra u oración completa.

 Para hacer frente a este problema, Aspose.Cells proporciona[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) propiedad que se debe establecer**verdadero**de modo que solo se cambie la fuente del carácter específico que no se puede mostrar y la fuente para el resto de la palabra u oración permanezca igual.

{{% /alert %}}

## **Ejemplo**

 La siguiente captura de pantalla compara los dos PDF de salida generados por el código de muestra a continuación. Uno fue generado sin configurar[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) propiedad y la otra se generó después de establecer la[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) propiedad a**verdadero**. Como puede ver en el primer PDF, la fuente de toda la oración ha cambiado de Times New Roman a Arial Unicode MS debido a Non-Breaking Hyphen. Mientras que en el segundo PDF, solo ha cambiado la fuente de Non-Breaking Hyphen.

![todo:imagen_alternativa_texto](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
