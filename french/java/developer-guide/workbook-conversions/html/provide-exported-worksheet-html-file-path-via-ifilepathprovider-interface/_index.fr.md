---
title: Fournir le chemin d'accès au fichier HTML de la feuille de calcul exportée via l'interface IFilePathProvider
type: docs
weight: 870
url: /fr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Scénarios d'utilisation possibles**
 Supposons que vous ayez un fichier Excel avec plusieurs feuilles et que vous souhaitiez exporter chaque feuille vers un fichier HTML individuel. Si l'une de vos feuilles contient des liens vers d'autres feuilles, ces liens seront rompus dans le code HTML exporté. Pour faire face à ce problème, le Aspose.Cells fournit[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)interface que vous pouvez implémenter pour réparer les liens rompus.
## **Fournir le chemin d'accès au fichier HTML de la feuille de calcul exportée via l'interface IFilePathProvider**
 Veuillez télécharger le[exemple de fichier excel](5473417.zip) utilisé dans le code suivant et ses fichiers HTML exportés. Tous ces fichiers sont à l'intérieur du*Temp* annuaire. Vous devriez l'extraire sur*C :* conduire. Il deviendra alors*C:\Temp*annuaire. Ensuite, vous ouvrirez le*Sheet1.html* fichier dans le navigateur et cliquez sur les deux liens à l'intérieur. Ces liens font référence à ces deux feuilles de calcul HTML exportées qui se trouvent dans le*C:\Temp\AutresFeuilles*annuaire.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La capture d'écran suivante montre comment le*C:\Temp\Feuille1.html*et ses liens ressemblent à

![tâche : image_autre_texte](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 La capture d'écran suivante montre la source HTML. Comme vous pouvez le voir, les liens font maintenant référence à*C:\Temp\AutresFeuilles* annuaire. Ceci a été réalisé en utilisant le[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)interface.

![tâche : image_autre_texte](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Exemple de code**
 Veuillez noter*C:\Temp* répertoire est juste à des fins d'illustration. Vous pouvez utiliser n'importe quel répertoire de votre choix et de votre lieu[exemple de fichier excel](5473414.xlsx) à l'intérieur et exécutez l'exemple de code fourni. Il créera alors*AutresFeuilles* sous-répertoire à l'intérieur de votre répertoire et exportez les deuxième et troisième feuilles de calcul HTML à l'intérieur. Veuillez changer le*dirPath*variable à l'intérieur du code fourni et référez-la au répertoire de votre choix avant l'exécution.

{{% alert color="primary" %}} 

L'exemple de code ne fonctionnera que lorsque vous définirez la licence Aspose.Cells. Si vous essayez d'exécuter le code sans définir la licence, il entrera dans une boucle infinie. Par conséquent, nous avons ajouté une vérification pour imprimer un message et arrêter l'exécution lorsque la licence n'est pas définie. Vous pouvez soit acheter une licence, soit demander une licence temporaire de 30 jours auprès de l'équipe Aspose.Purchase.

{{% /alert %}} 

 S'il vous plaît voir commenter ces lignes à l'intérieur du code cassera les liens dans*Sheet1.html* et*Sheet2.html* ou*Sheet3.html*ne s'ouvriront pas lorsque leurs liens seront cliqués à l'intérieur du*Sheet1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 Voici l'exemple de code complet que vous pouvez exécuter avec le fichier fourni[exemple de fichier excel](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
