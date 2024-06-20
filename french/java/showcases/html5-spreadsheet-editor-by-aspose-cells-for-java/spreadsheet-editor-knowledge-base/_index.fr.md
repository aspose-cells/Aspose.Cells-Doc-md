---
title: Base de connaissances de l éditeur de feuilles de calcul
type: docs
weight: 30
url: /fr/java/spreadsheet-editor-knowledge-base/
---

## **Intégrer HTML5 Spreadsheet Editor n'importe où**

HTML5 Spreadsheet Editor peut être intégré dans n'importe quel site Web, blog et forum pour partager des feuilles de calcul sur Internet. Il peut être intégré en tant qu'éditeur autonome ou vous pouvez le charger avec un fichier de feuille de calcul.

**Intégrer en tant qu'éditeur autonome**

Pour intégrer en tant qu'éditeur autonome, utilisez la balise HTML IFRAME à ajouter dans le site Web. Par exemple:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Intégrer avec une feuille de calcul**

Pour charger une feuille de calcul dans un éditeur intégré, utilisez le paramètre **url**. Par exemple:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
