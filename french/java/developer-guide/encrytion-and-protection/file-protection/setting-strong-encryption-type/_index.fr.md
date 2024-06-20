---
title: Définition du type de chiffrement fort
type: docs
weight: 10
url: /fr/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) vous permet de crypter et protéger par mot de passe des feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques. Un fournisseur de services cryptographiques (ou CSP) est un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est "Compatible avec Office 97/2000". Il s'agit d'un CSP avec des problèmes de sécurité publiquement connus. Les feuilles de calcul sécurisées avec le type de chiffrement "faible (XOR)" ou avec le type de chiffrement "Compatible avec Office 97/2000" peuvent être facilement craquées.

Pour remédier à ce problème, utilisez l'un des types de chiffrement forts fournis par Microsoft Excel. Vous pouvez changer le type de chiffrement pour le CSP le plus fort disponible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise, par exemple 'Fournisseur cryptographique fort Microsoft'.

Vous pouvez également chiffrer et protéger par mot de passe des fichiers Excel avec un type de chiffrement fort en utilisant l'API Aspose.Cells.

{{% /alert %}}

## **Application du chiffrement avec Microsoft Excel**

Pour implémenter le chiffrement de fichier dans Microsoft Excel (par exemple 2007) :

1. Dans le menu **Outils**, sélectionnez **Options**.
1. Sélectionnez l'onglet **Sécurité**.
1. Entrez une valeur pour le champ **Mot de passe pour ouvrir**.
1. Cliquez sur **Avancé**.
1. Choisissez le type de chiffrement et confirmez le mot de passe.

   **Paramétrer le chiffrement dans Microsoft Excel**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Application du chiffrement avec Aspose.Cells**

L'exemple de code ci-dessous applique un chiffrement fort à un fichier et définit un mot de passe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
