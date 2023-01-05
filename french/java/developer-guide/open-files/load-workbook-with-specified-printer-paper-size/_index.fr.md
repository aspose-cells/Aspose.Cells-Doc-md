---
title: Charger le classeur avec le format de papier d'imprimante spécifié
type: docs
weight: 790
url: /fr/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 Vous pouvez spécifier le format de papier d'imprimante de votre choix lors du chargement de votre classeur à l'aide de la[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) méthode. Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous constaterez que le format de papier est le même que le paramètre d'imprimante par défaut de votre machine.

{{% /alert %}} 
## **Charger le classeur avec le format de papier d'imprimante spécifié**
 L'exemple de code suivant illustre l'utilisation de[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) méthode. Il crée d'abord un classeur, puis l'enregistre dans un flux de tableau d'octets au format XLSX. Ensuite, il le charge avec du papier au format A5 et l'enregistre au format PDF. Ensuite, il le charge à nouveau avec un format de papier A3 et l'enregistre à nouveau au format PDF. Si vous ouvrez les fichiers PDF de sortie et vérifiez leur format de papier, vous verrez qu'ils sont différents. L'un est A5 et l'autre est A3. Veuillez télécharger le[Sortie A5 PDF](5473435.pdf) et[Sortie A3 PDF](5473436.pdf) généré par le code pour votre référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
