---
title: Gérer les codes VBA du classeur Excel compatible avec les macros.
linktitle: Macro-projet
type: docs
weight: 200
url: /fr/net/manage-vba-project/
description: Ajoutez un module VBA et modifiez VBA ou une macro avec la bibliothèque Aspose.Cells.
---
## **Ajouter un module VBA dans C#**
{{% alert color="primary" %}}

 Aspose.Cells vous permet d'ajouter un nouveau module VBA et un code macro à l'aide de Aspose.Cells. Veuillez utiliser le[**Classeur.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) méthode pour ajouter le nouveau module VBA dans le classeur

{{% /alert %}}

L'exemple de code suivant crée un nouveau classeur et ajoute un nouveau module VBA et un code de macro et enregistre la sortie au format XLSM. Une fois, vous ouvrirez le fichier de sortie XLSM dans Microsoft Excel et cliquez sur le**Développeur > Visual Basic** commandes de menu, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code macro suivant.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Voici l'exemple de code pour générer le fichier de sortie XLSM avec le module VBA et le code macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modifier VBA ou Macro dans C#**

{{% alert color="primary" %}} 

Vous pouvez modifier VBA ou le code macro à l'aide de Aspose.Cells. Aspose.Cells a ajouté l'espace de noms et les classes suivants pour lire et modifier le projet VBA dans le fichier Excel.

- Aspose.Cells.Vba
- Projet Vba
- VbaModuleCollectionVbaModuleCollection
- Module Vba

Cet article vous montrera comment modifier le code VBA ou macro dans le fichier Excel source à l'aide de Aspose.Cells.

{{% /alert %}} 

L'exemple de code suivant charge le fichier Excel source qui contient un code VBA ou Macro suivant à l'intérieur

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Après l'exécution de l'exemple de code Aspose.Cells, le code VBA ou Macro sera modifié comme ceci

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Vous pouvez télécharger le[fichier Excel source](5112508.xlsm) et le[fichier Excel de sortie](5112511.xlsm) à partir des liens donnés.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Sujets avancés**
- [Ajouter une référence de bibliothèque au projet VBA dans le classeur](/cells/fr/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Affecter une macro au contrôle de formulaire](/cells/fr/net/assign-macro-to-form-control/)
- [Vérifiez si la signature numérique du code VBA est valide](/cells/fr/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Vérifiez si le code VBA est signé](/cells/fr/net/check-if-vba-code-is-signed/)
- [Vérifier si le projet VBA dans un classeur est signé](/cells/fr/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Vérifiez si le projet VBA est protégé et verrouillé pour l'affichage](/cells/fr/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copier la macro VBA UserForm DesignerStorage du modèle au classeur cible](/cells/fr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signer numériquement un projet de code VBA avec certificat](/cells/fr/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exporter le certificat VBA vers un fichier ou un flux](/cells/fr/net/export-vba-certificate-to-file-or-stream/)
- [Filtrer le projet VBA lors du chargement d'un classeur](/cells/fr/net/filter-vba-project-while-loading-a-workbook/)
- [Découvrez si le projet VBA est protégé](/cells/fr/net/find-out-if-vba-project-is-protected/)
- [Mot de passe protéger le projet VBA du classeur Excel](/cells/fr/net/password-protect-the-vba-project-of-excel-workbook/)

