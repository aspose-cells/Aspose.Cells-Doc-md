---
title: Fournir le chemin d'accès au fichier html de la feuille de calcul exportée via l'interface IFilePathProvider
type: docs
weight: 70
url: /fr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Scénarios d'utilisation possibles**
 Supposons que vous ayez un fichier Excel avec plusieurs feuilles et que vous souhaitiez exporter chaque feuille vers un fichier HTML individuel. Si l'une de vos feuilles contient des liens vers d'autres feuilles, ces liens seront rompus dans le code HTML exporté. Pour faire face à ce problème, le Aspose.Cells fournit[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)interface que vous pouvez implémenter pour réparer les liens rompus.
## **Fournir le chemin d'accès au fichier HTML de la feuille de calcul exportée via l'interface IFilePathProvider**
 Veuillez télécharger le[exemple de fichier excel](5115213.zip)utilisé dans le code suivant et ses fichiers HTML exportés. Tous ces fichiers se trouvent dans le répertoire Temp. Vous devez l'extraire sur le lecteur C:. Ensuite, il deviendra le répertoire C:\Temp. Ensuite, vous ouvrirez le fichier Sheet1.html dans le navigateur et cliquerez sur les deux liens qu'il contient. Ces liens font référence à ces deux feuilles de calcul HTML exportées qui se trouvent dans le répertoire C:\Temp\OtherSheets.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La capture d'écran suivante montre à quoi ressemble C:\Temp\Sheet1.html et ses liens

![tâche : image_autre_texte](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 La capture d'écran suivante montre la source HTML. Comme vous pouvez le voir, les liens font maintenant référence au répertoire C:\Temp\OtherSheets. Ceci a été réalisé en utilisant le[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)interface.

![tâche : image_autre_texte](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Exemple de code**
 Veuillez noter que le répertoire C:\Temp est uniquement à des fins d'illustration. Vous pouvez utiliser n'importe quel répertoire de votre choix et de votre lieu[exemple de fichier excel](5115211.xlsx)à l'intérieur et exécutez l'exemple de code fourni. Il créera ensuite un sous-répertoire OtherSheets dans votre répertoire et exportera les deuxième et troisième feuilles de calcul HTML à l'intérieur. Veuillez modifier la variable dirPath dans le code fourni et la référer au répertoire de votre choix avant l'exécution.

{{% alert color="primary" %}} 

L'exemple de code ne fonctionnera que lorsque vous définirez la licence Aspose.Cells. Si vous essayez d'exécuter le code sans définir la licence, il entrera dans une boucle infinie. Par conséquent, nous avons ajouté une vérification pour imprimer un message et arrêter l'exécution lorsque la licence n'est pas définie. Vous pouvez soit acheter une licence, soit demander une licence temporaire de 30 jours auprès de l'équipe Aspose.Purchase.

{{% /alert %}} 

Veuillez voir commenter ces lignes à l'intérieur du code cassera les liens dans Sheet1.html et Sheet2.html ou Sheet3.html ne s'ouvrira pas lorsque leurs liens seront cliqués à l'intérieur de Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Voici l'exemple de code complet que vous pouvez exécuter avec le fourni[exemple de fichier excel](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
