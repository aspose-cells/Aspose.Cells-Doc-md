---
title: Comment installer les polices TrueType sous Linux
type: docs
weight: 20
url: /fr/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

Le scénario le plus probable est que vous utilisez Aspose.Cells pour convertir des feuilles de calcul en PDF. Si vous effectuez cette opération sur un système d'exploitation non basé sur Windows tel que Linux, cette rubrique explique comment vous assurer que Aspose.Cells restitue vos feuilles de calcul avec la meilleure fidélité.

Pour vous assurer que les feuilles de calcul converties par Aspose.Cells apparaissent aussi proches que possible de l'original, vous devrez peut-être installer les "polices Windows" ou les "polices TrueType" sur votre système Linux, car les polices TrueType les plus couramment utilisées ne sont pas préinstallées avec Distributions Linux par défaut.

Il existe deux manières principales d'obtenir des polices TrueType sur un système Linux :

1. Copiez les fichiers de police (.TTF et .TTC) d'une machine Windows vers votre machine Linux.
1. Installez un package de polices TrueType, tel que msttcorefonts.

{{% /alert %}}

## **Copier des polices à partir d'une machine Windows**

Un moyen simple et rapide consiste à copier les fichiers .TTF et .TTC du répertoire C:\Windows\Fonts sur une machine Windows vers un répertoire sur votre machine Linux. Vous n'avez en aucun cas besoin d'installer ou d'enregistrer ces polices sur Linux, il vous suffit de spécifier l'emplacement des polices à l'aide de la méthode FontConfigs.setFontFolder dans votre application.

{{% alert color="primary" %}}

Pour autant que nous sachions, Microsoft autorise les polices à n'importe qui à les utiliser librement, mais veuillez vérifier la licence des polices par vous-même.

{{% /alert %}}

## **Installer un package de polices TrueType**

Les informations fournies ci-dessous vous guideront étape par étape pour installer les polices TrueType les plus célèbres du Microsoft sur les distributions Linux telles que Fedora et Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Vous pouvez avoir besoin de privilèges de niveau 'root', donc connectez-vous en tant que 'root' ou configurez sudo.

{{% /alert %}}

Voici comment procéder à l'aide du Terminal.

1. Assurez-vous que les packages RPM suivants sont installés.
   1. **rpm-build**: S'il n'est pas installé, utilisez la commande suivante pour installer le package rpm-build

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: S'il n'est pas installé, utilisez la commande suivante

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. Téléchargez le dernier fichier de spécification msttcorefonts à partir de SourceForge à l'aide de la commande suivante,

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Construisez un fichier RPM en utilisant le fichier de spécification précédemment téléchargé et la commande suivante,

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Le fichier RPM sera stocké dans : /root/rpmbuild/RPMS/noarch/, installez-le comme suit,

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Redémarrez la machine pour que les modifications prennent effet.

Les instructions fournies ci-dessus installeront le package TTF Microsoft comprenant les familles de polices suivantes :

1. Andale Mono
1. Arial Noir/Arial (gras, italique, gras italique)
1. Comic Sans MS (Gras)
1. Courier New (gras, italique, gras italique)
1. Géorgie (gras, italique, gras italique)
1. Impacter
1. Tahoma
1. Times New Roman (gras, italique, gras italique)
1. Trébuchet (gras, italique, gras italique)
1. Verdana (gras, italique, gras italique)
1. Sangles

{{% alert color="primary" %}}

 Sur Ubuntu, accédez au gestionnaire de paquets Synaptic. Trouvez et installez le**ttf-mscorefonts-installer** forfait.

{{% /alert %}}
