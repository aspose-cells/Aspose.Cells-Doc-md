---
title: Gérer les codes VBA du classeur activé par macro Excel.
linktitle: Projet de macro
type: docs
weight: 200
url: /fr/net/manage-vba-project/
description: Ajouter un module VBA et modifier le VBA ou la macro avec la bibliothèque Aspose.Cells.
---

## **Ajouter un module VBA en C#**
{{% alert color="primary" %}}

Aspose.Cells vous permet d'ajouter un nouveau module VBA et un code de macro en utilisant Aspose.Cells. Veuillez utiliser la méthode [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) pour ajouter le nouveau module VBA à l'intérieur du classeur.

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur et ajoute un nouveau module VBA et un code de macro, puis enregistre la sortie au format XLSM. Une fois, vous ouvrirez le fichier XLSM de sortie dans Microsoft Excel et cliquerez sur les commandes de menu **Développeur > Visual Basic**, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code de macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Voici le code d'exemple pour générer le fichier XLSM de sortie avec un module VBA et un code de macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modifier le VBA ou la macro en C#**

{{% alert color="primary" %}} 

Vous pouvez modifier le code VBA ou macro en utilisant Aspose.Cells. Aspose.Cells a ajouté l'espace de noms et les classes suivants pour lire et modifier le projet VBA dans le fichier Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Cet article vous montrera comment modifier le code VBA ou Macro à l'intérieur du fichier Excel source en utilisant Aspose.Cells.

{{% /alert %}} 

Le code d'exemple suivant charge le fichier Excel source qui contient un code VBA ou Macro à l'intérieur

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Après l'exécution du code d'exemple Aspose.Cells, le code VBA ou Macro sera modifié comme ceci

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Vous pouvez télécharger le [fichier Excel source](5112508.xlsm) et le [fichier Excel de sortie](5112511.xlsm) à partir des liens donnés.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Sujets avancés**
- [Ajouter une référence de bibliothèque au projet VBA dans le classeur](/cells/fr/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Attribuer une macro à un contrôle de formulaire](/cells/fr/net/assign-macro-to-form-control/)
- [Vérifier si la signature numérique du code VBA est valide](/cells/fr/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Vérifier si le code VBA est signé](/cells/fr/net/check-if-vba-code-is-signed/)
- [Vérifier si le projet VBA dans un classeur est signé](/cells/fr/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Vérifier si le projet VBA est protégé et verrouillé pour la visualisation](/cells/fr/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible](/cells/fr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signer numériquement un projet de code VBA avec un certificat](/cells/fr/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exporter le certificat VBA vers un fichier ou un flux](/cells/fr/net/export-vba-certificate-to-file-or-stream/)
- [Filtrer le projet VBA lors du chargement d'un classeur](/cells/fr/net/filter-vba-project-while-loading-a-workbook/)
- [Découvrir si le projet VBA est protégé](/cells/fr/net/find-out-if-vba-project-is-protected/)
- [Protéger par mot de passe le projet VBA du classeur Excel](/cells/fr/net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="csharp" >}}
