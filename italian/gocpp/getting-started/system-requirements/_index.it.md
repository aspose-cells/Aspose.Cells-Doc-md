---
title: Requisiti di sistema
type: docs
weight: 30
url: /it/go-cpp/system-requirements/
---

Aspose.Cells for Go via C++ è una libreria Go nativa che permette agli sviluppatori di Go di creare, manipolare e convertire fogli di calcolo programmaticamente senza necessità di Office Automation o Microsoft Excel.

## Sistemi operativi supportati

Aspose.Cells per Go supporta i seguenti sistemi operativi a 64-bit e piattaforme:

<table>  
 <tr>
   <td style="font-weight: bold; width:400px">Sistema operativo</td>
   <td style="font-weight: bold; width:400px">Versioni</td>
  </tr>
  <tr>
   <td>Microsoft Windows</td>
   <!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
   <td><ul><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
   <td>Linux</td>
   <td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 o successivi</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---></ul></td>
  </tr>
</table>

## Ambiente di sviluppo

Puoi usare Aspose.Cells for Go via C++ per sviluppare applicazioni per Windows, Linux.

### Windows

Aspose.Cells for Go via C++ può essere utilizzato per sviluppare applicazioni in qualsiasi ambiente di sviluppo che supporta [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/go/porting/binary-compat-2015-2017?view=msvc-160), ma gli ambienti elencati nella tabella seguente sono esplicitamente supportati:

### Linux

Aspose.Cells for Go via C++ può essere utilizzato per sviluppare applicazioni nell’ambiente di sviluppo che supporta Go 1.13 o superiore, ma i compilatori e gli strumenti seguenti sono esplicitamente supportati:

<table>  
 <tr>
   <td style="font-weight: bold; width:800px">Compilatori</td>
  </tr>
  <tr>
   <td><ul><li>GCC 9.4.0 o successivo</li></ul></td>
   </tr>
</table>

### Dipendenza aggiuntiva su Linux

Aspose.Cells for Go on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`
