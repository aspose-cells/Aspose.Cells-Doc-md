---
title: Comment installer une police sous Linux
type: docs
description: "Comment installer une police sous Linux"
weight: 139
url: /fr/net/how-to-install-font-in-linux/
---

## Aperçu

Lorsque vous utilisez Aspose.Cells sous Linux, étant donné que Linux a moins de polices par défaut, la police référencée dans votre fichier Excel peut ne pas exister par défaut sur votre système Linux.
Lorsque cela se produit, Aspose.Cells utilisera une police similaire pour afficher les caractères. Cependant, cela peut entraîner les effets suivants :

1. Des polices différentes peuvent entraîner des images rendues dans des dispositions différentes de celles dans Excel.
2. Étant donné que la police a changé, les caractères de sortie peuvent ne pas répondre à vos attentes.

Pour que votre programme produise des résultats plus précis, installez les polices dont vous avez besoin sous Linux. Il est important de s'assurer que les polices que vous utilisez dans les fichiers Excel existent dans votre environnement.

## Comment installer une police sous Linux

Il existe deux façons d'installer des polices sous Linux, comme décrites ci-dessous :

### Copier les fichiers de police dans le chemin système Linux

1. Placez un dossier nommé "polices" dans le répertoire de votre programme, copiez les fichiers de police dont vous avez besoin dans ce dossier.
2. Ajoutez la commande suivante dans votre Dockerfile Linux :
```
COPY fonts/ /usr/share/fonts
```
3. Après cette opération, les fichiers de police seront copiés dans le chemin système Linux. Aspose.Cells accédera au chemin système pour les trouver et les utiliser. C’est notre scénario recommandé.

### Définir le dossier de police avec l’API Aspose.Cells
Dans certains cas, vous ne pouvez pas contrôler ou modifier le répertoire système Linux. Par exemple, sur des serveurs cloud. Dans ce cas, vous pouvez utiliser le deuxième scénario.
1. Placez un dossier nommé "fonts" dans le répertoire de votre programme et copiez-y les fichiers de police dont vous avez besoin.
2. Dans votre code de programme, appelez l'API Aspose.Cells :
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. L'opération ci-dessus garantira que le programme peut trouver la police depuis le chemin du projet.

## Voir aussi

- [Comment exécuter Aspose.Cells pour .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
