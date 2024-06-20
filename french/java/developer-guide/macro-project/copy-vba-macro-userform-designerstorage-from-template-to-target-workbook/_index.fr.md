---
title: Copier le UserForm DesignerStorage du macro VBA du modèle vers le classeur cible
type: docs
weight: 60
url: /fr/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de copier le projet VBA d'un fichier Excel dans un autre fichier Excel. Le projet VBA se compose de différents types de modules tels que Document, Procédural, Designer, etc. Tous les modules peuvent être copiés avec un code simple, mais pour le module Designer, il y a des données supplémentaires appelées Designer Storage qui doivent être accédées ou copiées. Les deux méthodes suivantes traitent de Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible**

Veuillez consulter le code d'exemple suivant. Il copie le projet VBA du fichier Excel de modèle dans un classeur vide et l'enregistre sous le nom de fichier Excel de sortie. Si vous ouvrez le projet VBA à l'intérieur du fichier Excel de modèle, vous verrez un formulaire utilisateur comme indiqué ci-dessous. Le formulaire utilisateur se compose d'un stockage de concepteur, donc il sera copié à l'aide des méthodes [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) et [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])).

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

La capture d'écran suivante montre le fichier Excel de sortie et son contenu qui ont été copiés à partir du fichier Excel modèle. Lorsque vous cliquez sur le Bouton 1, il ouvre le formulaire utilisateur VBA qui contient lui-même un bouton de commande qui affiche une boîte de message lorsque vous cliquez dessus.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
