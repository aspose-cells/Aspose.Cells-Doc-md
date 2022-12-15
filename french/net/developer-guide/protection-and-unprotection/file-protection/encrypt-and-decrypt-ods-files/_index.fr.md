---
title: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/net/encrypt-and-decrypt-ods-files/
description: protégez par mot de passe et cryptez les fichiers ODS en utilisant Aspose.Cells pour .Net qui est une pure bibliothèque net.
---
{{% alert color="primary" %}}
 OpenOffice.org est une suite bureautique complète qui prend en charge la protection par mot de passe et le cryptage des fichiers. Cependant, le fichier ODS crypté ne peut être ouvert par OpenOffice qu'après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS crypté et peut générer un message d'avertissement. Les options de cryptage ne s'appliquent pas au fichier ODS contrairement aux autres types de fichiers.
 Aspose.Cells permet de chiffrer et de déchiffrer le fichier ODS. Le fichier ODS décrypté peut être ouvert à la fois dans Excel et OpenOffice,
{{% /alert %}}

## **Crypter avec OpenOffice Calc**
1.  Sélectionner**Enregistrer sous** et cliquez sur le**Enregistrer avec mot de passe** boîte.
1.  Clique le**sauvegarder** bouton.
1.  Tapez votre mot de passe souhaité dans les deux**Entrez le mot de passe pour ouvrir** et**Confirmez le mot de passe** champs dans la fenêtre Définir le mot de passe qui s'ouvre.
1.  Clique le**D'ACCORD** bouton pour enregistrer le fichier.

## **Crypter le fichier ODS avec Aspose.Cells pour .Net**
 Pour chiffrer un fichier ODS, chargez le fichier et définissez le[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) valeur au mot de passe réel avant de l'enregistrer. Le fichier ODS crypté de sortie ne peut être ouvert que dans OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Décrypter le fichier ODS avec Aspose.Cells pour .Net**

 Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Une fois le fichier chargé, réglez le[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) chaîne à null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
