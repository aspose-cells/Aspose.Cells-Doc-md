---
title: Comment exécuter Aspose.Cells pour Python via .NET dans Docker
type: docs
description: « Exécuter Aspose.Cells dans un conteneur Docker pour Linux »
weight: 140
url: /fr/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Préface :

De plus en plus d’utilisateurs utilisent différents produits de notre entreprise dans Docker, et rencontrent diverses problématiques. Cet article présente brièvement comment utiliser Aspose.Cells pour Python via .NET dans un environnement Docker basé sur Debian Linux.

## Exemple :

Nous illustrons l’utilisation avec un exemple simple. Dans ce cas, la fonctionnalité est très directe, il suffit d’ouvrir un fichier Excel contenant du texte japonais dans aspose_test.py. Ici, nous utilisons python:3.11 comme image de base, et le Dockerfile correspondant est le suivant :

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

Ensuite, lorsque nous exécutons la commande suivante, nous obtenons le résultat final :
- Construire l'image Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Exécuter l'image Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Remarque :

Pour prendre en charge l'ouverture de fichiers Excel contenant diverses langues, nous devons installer ICU. Étant donné que le wrapper Python via .NET est basé sur .NET Core 3.1, et que .NET Core 3.1 a des exigences spécifiques de versions pour ICU, qui ne doivent pas dépasser la version 70, nous devons installer une version spécifique d'ICU.


## Voir aussi

- [Installer Docker Desktop sur Windows](https://docs.docker.com/docker-for-windows/install/)
