---
title: Charger le classeur avec la taille de papier de l imprimante spécifiée
type: docs
weight: 790
url: /fr/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Vous pouvez spécifier la taille de papier de l'imprimante de votre choix lors du chargement de votre classeur en utilisant la méthode [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous constaterez que la taille du papier est la même que la configuration de l'imprimante par défaut sur votre machine.

{{% /alert %}} 
## **Charger le classeur avec une taille de papier d'imprimante spécifiée**
Le code d'exemple suivant illustre l'utilisation de la méthode [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Il crée d'abord un classeur, puis l'enregistre dans un flux de tableau d'octets au format XLSX. Ensuite, il le charge avec une taille de papier A5 et l'enregistre au format PDF. Ensuite, il le charge à nouveau avec une taille de papier A3 et l'enregistre à nouveau au format PDF. Si vous ouvrez les PDF de sortie et vérifiez leur taille de papier, vous verrez qu'ils sont différents. L'un est en A5 et l'autre en A3. Veuillez télécharger les [PDF de sortie en A5](5473435.pdf) et [PDF de sortie en A3](5473436.pdf) générés par le code pour votre référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
