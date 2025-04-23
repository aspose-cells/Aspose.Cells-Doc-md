---
title: Charger le classeur avec la taille de papier de l imprimante spécifiée
type: docs
weight: 790
url: /fr/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Vous pouvez spécifier la taille du papier de l'imprimante de votre choix lors du chargement du classeur en utilisant la méthode [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Notez que si vous créez un nouveau fichier dans MS Excel, vous constaterez que la taille du papier est la même que celle du paramètre par défaut de votre imprimante.

{{% /alert %}} 
## **Charger le classeur avec une taille de papier d'imprimante spécifiée**
Le code exemple suivant illustre l'utilisation de la méthode [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Il commence par créer un classeur, puis le sauvegarde dans un flux de tableau d'octets au format XLSX. Ensuite, il le charge avec une taille de papier A5 puis le sauvegarde au format PDF. Ensuite, il le recharge avec une taille de papier A3 et le sauvegarde à nouveau en PDF. Si vous ouvrez les PDF de sortie et vérifiez leur taille de papier, vous verrez qu'elles sont différentes. L'une est A5 et l'autre A3. Veuillez télécharger le [PDF de sortie A5](5473435.pdf) et le [PDF de sortie A3](5473436.pdf) générés par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
