# Do not modify this file!  It was generated by ‘nixos-generate-config’
# and may be overwritten by future invocations.  Please make changes
# to /etc/nixos/configuration.nix instead.
{ config, lib, pkgs, modulesPath, ... }:

{
  imports =
    [ (modulesPath + "/installer/scan/not-detected.nix")
    ];

  boot.initrd.availableKernelModules = [ "xhci_pci" "nvme" "usb_storage" "uas" "usbhid" "sd_mod" "rtsx_pci_sdmmc" ];
  boot.initrd.kernelModules = [ "dm-snapshot" ];
  boot.initrd.luks.devices = {
    root = {
      device = "/dev/disk/by-uuid/f9df4fdd-3fdb-4f40-bf26-5003fbc111ac";
      preLVM = true;
      allowDiscards = true;
    };
  };

  boot.kernelModules = [ "kvm-intel" ];
  boot.extraModulePackages = [ ];

  fileSystems."/" =
    { device = "/dev/disk/by-uuid/3b87a68b-665e-4f33-89f5-b3564120fd09";
      fsType = "ext4";
    };

  fileSystems."/boot" =
    { device = "/dev/disk/by-uuid/F09A-52A7";
      fsType = "vfat";
    };

  swapDevices = [ ];

  # disable broken USB port in hub. Probably not needed with a different hub.
  services.udev.extraRules = ''
    KERNELS=="usb4" SUBSYSTEMS=="usb" ATTRS{idVendor}=="1d6b" ATTRS{idProduct}=="0003" ATTR{authorized}="0"
  '';

  powerManagement.cpuFreqGovernor = lib.mkDefault "powersave";
  hardware.cpu.intel.updateMicrocode = lib.mkDefault config.hardware.enableRedistributableFirmware;
  # high-resolution display
  hardware.video.hidpi.enable = lib.mkDefault true;
}
