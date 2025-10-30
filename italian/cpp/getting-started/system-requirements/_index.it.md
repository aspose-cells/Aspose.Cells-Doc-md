---
title: Requisiti di sistema
type: docs
weight: 30
url: /it/cpp/system-requirements/
---

Aspose.Cells for C++ è una libreria nativa C++ che consente ai programmatori C++ di creare, manipolare e convertire fogli di calcolo in modo programmatico senza richiedere l'automazione di Office o l'applicazione Microsoft Excel.

## Sistemi operativi supportati

Aspose.Cells for C++ supporta i seguenti sistemi operativi e piattaforme a 64 o 32 bit:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Sistema operativo</td>
			<td style="font-weight: bold; width:400px">Versioni</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64 </li><!---li> Ubuntu 20.04 o successiva </li><li> Fedora </li><li> OpenSUSE </li><li> CentOS </li---><li> Linux per ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 o successiva (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Ambiente di sviluppo

Puoi utilizzare Aspose.Cells for C++ durante lo sviluppo di applicazioni per Windows, Linux o macOS.

### Windows

Aspose.Cells for C++ può essere utilizzato per sviluppare applicazioni in qualsiasi ambiente di sviluppo che supporti [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), ma gli ambienti elencati nella tabella seguente sono supportati esplicitamente:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Ambienti di sviluppo</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ può essere utilizzato per sviluppare applicazioni nell'ambiente di sviluppo che supporta C++11 o versioni successive, ma il seguente compilatore e strumento sono supportati esplicitamente:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compilatori</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 o successivo</li></ul></td>
			</tr>
</table>

### Dipendenza aggiuntiva su Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ può essere utilizzato per sviluppare applicazioni negli ambienti di sviluppo seguenti:
* Xcode 12.5.1 o successivo
* Clang e libc++ (che sono inclusi per default con Xcode)
{{< app/cells/assistant language="cpp" >}}
