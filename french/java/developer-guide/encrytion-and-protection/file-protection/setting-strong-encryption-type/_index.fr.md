---
title: Définition du type de cryptage fort
type: docs
weight: 10
url: /fr/java/setting-strong-encryption-type/
---
{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) vous permet de crypter et de protéger par mot de passe les feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques. Un fournisseur de services cryptographiques (ou CSP) est un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est "Compatible avec Office 97/2000". Il s'agit d'un CSP avec des problèmes de sécurité connus du public. Les feuilles de calcul sécurisées avec le "cryptage faible (XOR)" ou avec le type de cryptage "Compatible Office 97/2000" peuvent être piratées facilement.

Pour surmonter ce problème, utilisez l'un des types de cryptage fort fournis par Microsoft Excel. Vous pouvez modifier le type de cryptage pour le CSP disponible le plus puissant. Pour un cryptage fort, une longueur de clé minimale de 128 bits est requise, par exemple 'Microsoft Strong Cryptographic Provider'.

Vous pouvez également crypter et protéger par mot de passe les fichiers Excel avec un type de cryptage fort en utilisant le Aspose.Cells API.

{{% /alert %}}

## **Application du cryptage avec Microsoft Excel**

Pour implémenter le chiffrement de fichiers dans Microsoft Excel (par exemple 2007) :

1.  Du**Outils** menu, sélectionnez**Choix**.
1.  Sélectionnez le**Sécurité** languette.
1.  Entrez une valeur pour le**Mot de passe pour ouvrir** champ.
1.  Cliquez sur**Avancé**.
1. Choisissez le type de cryptage et confirmez le mot de passe.

   **Réglage du cryptage dans Microsoft Excel**

![tâche : image_autre_texte](setting-strong-encryption-type_1.png)

## **Application du cryptage avec Aspose.Cells**

L'exemple de code ci-dessous applique un cryptage fort sur un fichier et définit un mot de passe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
