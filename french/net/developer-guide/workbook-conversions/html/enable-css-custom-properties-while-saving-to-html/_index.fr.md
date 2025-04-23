---
title: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/net/enable-css-custom-properties-while-saving-to-html/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, pour le scénario où il y a plusieurs occurrences pour une image base64, avec une propriété personnalisée, les données de l'image n'ont besoin d'être enregistrées qu'une seule fois afin d'améliorer la performance du HTML résultant. Veuillez utiliser la propriété [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/EnableCssCustomProperties) et la définir sur **true** lors de l'enregistrement en HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/enablecsscustomproperties). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée sur true. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) utilisé dans ce code et le [HTML de sortie](50528261.zip) généré pour référence.



## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-EnableCssCustomProperties-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
