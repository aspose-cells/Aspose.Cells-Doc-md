+++
title = "How to Install TrueType Fonts on Linux" 
description = "" 
weight = 20371 
+++

Aspose.Cells for Java : How to Install TrueType Fonts on Linux  

# Aspose.Cells for Java : How to Install TrueType Fonts on Linux


The most likely scenario is that you are using Aspose.Cells to convert spreadsheets to PDF. If you are doing this on a non-Windows based operating system such as Linux then this topic explains how to ensure that Aspose.Cells renders your spreadsheets with best fidelity.

To make sure that spreadsheets converted by Aspose.Cells appears as close to the original as possible, you might need to install "Windows fonts" or "TrueType fonts" on your Linux system because the most commonly used TrueType fonts don’t come pre-installed with Linux distributions by default.

There are two main ways to get TrueType fonts on a Linux system:

1.  Copy font files (.TTF and .TTC) from a Windows machine to your Linux machine.
2.  Install a TrueType fonts package, such as msttcorefonts.

#### Copy Fonts from a Windows Machine

An easy and quick way is to copy .TTF and .TTC files from the C:\\Windows\\Fonts directory on a Windows machine to some directory on your Linux machine. You do not need to install or register these fonts on Linux in any way, you just need to specify the location of the fonts using the `FontConfigs.setFontFolder` method in your application.

As far as we can tell, Microsoft licenses the fonts for anyone to freely use them, but please check the font licensing for yourself.

#### Install a TrueType Fonts Package

Below provided information will guide you step by step to install the Microsoft's most famous TrueType fonts on Linux distributions such as Fedora and Red Hat Enterprise Linux (RHEL).

You may require 'root' level privileges therefore login as 'root' or get sudo configured.

Here’s how to do it using the Terminal.

1.  Make sure you have the following RPM packages installed.
    *   **rpm-build**: If not installed, use the following command to install the rpm-build package
        
        yum install rpm-build cabextract ttmkfdir
        
    *   **wget**: If not installed, use the following command
        
        yum \\-y install wget
        
2.  Download the latest msttcorefonts spec file from SourceForge using the command as follow,
    
    wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec
    
3.  Build a RPM file using the previously downloaded spec file and the following command,
    
    rpmbuild \\-ba msttcorefonts-2.5-1.spec
    
4.  The RPM file will be stored in: /root/rpmbuild/RPMS/noarch/, install it as follow,
    
    rpm \\-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm 
    
5.  Restart the machine to make the changes take effect.

The instructions provided above will install the Microsoft TTFs package including the following font-families:

1.  Andale Mono
2.  Arial Black/Arial (Bold, Italic, Bold Italic)
3.  Comic Sans MS (Bold)
4.  Courier New (Bold, Italic, Bold Italic)
5.  Georgia (Bold, Italic, Bold Italic)
6.  Impact
7.  Tahoma
8.  Times New Roman (Bold, Italic, Bold Italic)
9.  Trebuchet (Bold, Italic, Bold Italic)
10.  Verdana (Bold, Italic, Bold Italic)
11.  Webdings

On Ubuntu, go to the Synaptic Package Manager. Find and install the **ttf-mscorefonts-installer** package.

