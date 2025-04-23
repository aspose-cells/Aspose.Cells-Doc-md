---
title: Fournir le chemin du fichier HTML de la feuille de calcul exportée via l interface IFilePathProvider
type: docs
weight: 70
url: /fr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Scénarios d'utilisation possibles**
Supposez que vous ayez un fichier Excel avec plusieurs feuilles et que vous souhaitiez exporter chaque feuille dans un fichier HTML individuel. Si l'une de vos feuilles contient des liens vers d'autres feuilles, alors ces liens seront rompus dans le HTML exporté. Pour résoudre ce problème, Aspose.Cells fournit l'interface [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) que vous pouvez implémenter pour corriger les liens rompus.
## **Fournir le chemin du fichier HTML de la feuille de calcul exportée via l'interface IFilePathProvider**
Veuillez télécharger le [fichier Excel d'exemple](5115213.zip) utilisé dans le code suivant et ses fichiers HTML exportés. Tous ces fichiers sont à l'intérieur du répertoire Temp. Vous devez l'extraire sur le lecteur C: . Ensuite, cela deviendra le répertoire C:\Temp. Ensuite, vous ouvrirez le fichier Sheet1.html dans le navigateur et cliquerez sur les deux liens à l'intérieur. Ces liens font référence à ces deux feuilles de calcul HTML exportées qui se trouvent dans le répertoire C:\Temp\OtherSheets.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La capture d'écran suivante montre à quoi ressemblent le C:\Temp\Sheet1.html et ses liens

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La capture d'écran suivante montre la source HTML. Comme vous pouvez le voir, les liens font maintenant référence au répertoire C:\Temp\OtherSheets. Cela a été réalisé en utilisant l'interface [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Code d'exemple**
Veuillez noter que le répertoire C:\Temp est uniquement à des fins d'illustration. Vous pouvez utiliser n'importe quel répertoire de votre choix et placer le [fichier Excel d'exemple](5115211.xlsx) à l'intérieur et exécuter le code d'exemple fourni. Cela créera ensuite le sous-répertoire OtherSheets à l'intérieur de votre répertoire et exportera les feuilles de calcul HTML du deuxième et du troisième à l'intérieur. Veuillez modifier la variable dirPath à l'intérieur du code fourni et la faire référence au répertoire de votre choix avant l'exécution.

{{% alert color="primary" %}} 

Le code d'exemple ne fonctionnera que si vous définissez la licence Aspose.Cells. Si vous essayez d'exécuter le code sans définir la licence, il entrera dans une boucle infinie. Par conséquent, nous avons ajouté une vérification pour afficher un message et arrêter l'exécution lorsque la licence n'est pas définie. Vous pouvez acheter une licence ou demander une licence temporaire de 30 jours à l'équipe Aspose.Purchase.

{{% /alert %}} 

Veuillez noter que commenter ces lignes à l'intérieur du code rompra les liens dans Sheet1.html et Sheet2.html ou Sheet3.html ne s'ouvriront pas lorsque leurs liens seront cliqués à l'intérieur de Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Voici le code d'exemple complet que vous pouvez exécuter avec le [fichier Excel d'exemple](5115211.xlsx) fourni.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
