---
title: Requisiti di sistema
type: docs
weight: 30
url: /it/cpp/system-requirements/
---
Aspose.Cells for C++ è una libreria nativa C++ che consente agli sviluppatori C++ di creare, manipolare e convertire fogli di calcolo a livello di codice senza richiedere Office Automation o l'applicazione Excel Microsoft.

##  Sistemi operativi supportati

Aspose.Cells for C++ supporta i seguenti sistemi operativi e piattaforme a 64 bit o 32 bit:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Sistema operativo</td>
			<td style="font-weight: bold; width:400px">Versioni</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windowsx86</li><li>Windowsx86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linuxx86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux per ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>Mac OS</td>
			<td><ul><li>macOS 11 o successivo (arm64, x86_64)</li></ul></td>
		</tr>
</table>

##  Sviluppo dell'ambiente

Puoi utilizzare Aspose.Cells for C++ quando sviluppi applicazioni per Windows, Linux o macOS.

###  Windows

 Aspose.Cells for C++ può essere utilizzato per sviluppare applicazioni in qualsiasi ambiente di sviluppo che supporti[Microsoft Set di strumenti della piattaforma Visual Studio v142](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), ma gli ambienti elencati nella tabella seguente sono esplicitamente supportati:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Ambienti di sviluppo</td>
		</tr>
  <tr>
			<td><ul><li>MicrosoftVisual Studio 2019</li><li>MicrosoftVisual Studio 2022</li></ul></td>
			</tr>
</table>

###  Linux

Aspose.Cells for C++ può essere utilizzato per sviluppare applicazioni nell'ambiente di sviluppo che supporta C++11 o versione successiva, ma il seguente compilatore e strumento sono esplicitamente supportati:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compilatori</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 o successivo</li></ul></td>
			</tr>
</table>

###  Dipendenza aggiuntiva da Linux
 Aspose.Cells for C++ su Linux dipende da<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binari sia libreria dinamica che strumento. Si prega di installarlo prima dell'uso:

1. Installazione di fontconfig su Ubuntu o Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installazione di fontconfig su Fedora o CentOs<br>
`sudo yum install fontconfig`

###  Mac OS
Aspose.Cells for C++ può essere utilizzato per sviluppare applicazioni nei seguenti ambienti di sviluppo:
* Xcode 12.5.1 o successivo
* Clang e libc++ (forniti per impostazione predefinita con Xcode)
