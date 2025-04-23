---
title: Configuration requise
type: docs
weight: 30
url: /fr/go-cpp/system-requirements/
---

Aspose.Cells for Go via C++ est une bibliothèque Go native qui permet aux développeurs Go de créer, manipuler et convertir des feuilles de calcul de manière programmatique sans nécessiter l'automatisation Office ou l'application Microsoft Excel.

## Systèmes d'exploitation pris en charge

Aspose.Cells pour Go supporte les systèmes d'exploitation 64 bits et plateformes suivants :

<table>  
 <tr>
   <td style="font-weight: bold; width:400px">Système d'exploitation</td>
   <td style="font-weight: bold; width:400px">Versions</td>
  </tr>
  <tr>
   <td>Microsoft Windows</td>
   <!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
   <td><ul><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
   <td>Linux</td>
   <td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 ou version ultérieure</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---></ul></td>
  </tr>
</table>

## Environnement de développement

Vous pouvez utiliser Aspose.Cells for Go via C++ lors du développement d'applications pour Windows, Linux.

### Windows

Aspose.Cells for Go via C++ peut être utilisé pour développer des applications dans n'importe quel environnement de développement qui supporte [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/go/porting/binary-compat-2015-2017?view=msvc-160), mais les environnements listés dans le tableau suivant sont explicitement supportés :

### Linux

Aspose.Cells for Go via C++ peut être utilisé pour développer des applications dans l'environnement de développement qui supporte Go 1.13 ou supérieur, mais les compilateurs et outils suivants sont explicitement supportés :

<table>  
 <tr>
   <td style="font-weight: bold; width:800px">Compilateurs</td>
  </tr>
  <tr>
   <td><ul><li>GCC 9.4.0 ou ultérieur</li></ul></td>
   </tr>
</table>

### Dépendance supplémentaire sur Linux

Aspose.Cells for Go on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`
