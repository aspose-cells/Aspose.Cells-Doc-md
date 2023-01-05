---
title: Copier la macro VBA UserForm DesignerStorage du modèle au classeur cible
type: docs
weight: 60
url: /fr/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de copier le projet VBA d'un fichier Excel dans un autre fichier Excel. Le projet VBA se compose de différents types de modules, à savoir Document, Procédural, Designer, etc. Tous les modules peuvent être copiés avec un code simple, mais pour le module Designer, il existe des données supplémentaires appelées Designer Storage qui doivent être consultées ou copiées. Les deux méthodes suivantes traitent de Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Copier la macro VBA UserForm DesignerStorage du modèle au classeur cible**

Veuillez consulter l'exemple de code suivant. Il copie le projet VBA à partir du[modèle de fichier Excel](50528367.xlsm)dans un classeur vide et l'enregistre en tant que[fichier Excel de sortie](50528366.xlsm). Si vous ouvrez le projet VBA dans le fichier modèle Excel, vous verrez un formulaire utilisateur comme indiqué ci-dessous. Le formulaire utilisateur se compose de Designer Storage, il sera donc copié à l'aide de[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) et[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) méthodes.

![tâche : image_autre_texte](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

La capture d'écran suivante montre le fichier Excel de sortie et son contenu qui ont été copiés à partir du fichier modèle Excel. Lorsque vous cliquez sur le bouton 1, il ouvre le formulaire utilisateur VBA qui a lui-même un bouton de commande qui affiche une boîte de message en cliquant.

![tâche : image_autre_texte](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
