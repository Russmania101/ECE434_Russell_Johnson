#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x4062870e, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0xfe990052, __VMLINUX_SYMBOL_STR(gpio_free) },
	{ 0xf20dabd8, __VMLINUX_SYMBOL_STR(free_irq) },
	{ 0x7a49375a, __VMLINUX_SYMBOL_STR(gpiod_unexport) },
	{ 0xd6b8e852, __VMLINUX_SYMBOL_STR(request_threaded_irq) },
	{ 0xdbb79f8e, __VMLINUX_SYMBOL_STR(gpiod_to_irq) },
	{ 0x5137d5d0, __VMLINUX_SYMBOL_STR(gpiod_set_debounce) },
	{ 0xd7f31d7c, __VMLINUX_SYMBOL_STR(gpiod_direction_input) },
	{ 0x1d6bdc76, __VMLINUX_SYMBOL_STR(gpiod_export) },
	{ 0x57185d6a, __VMLINUX_SYMBOL_STR(gpiod_direction_output_raw) },
	{ 0x47229b5c, __VMLINUX_SYMBOL_STR(gpio_request) },
	{ 0x2e5810c6, __VMLINUX_SYMBOL_STR(__aeabi_unwind_cpp_pr1) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0xe8a41e28, __VMLINUX_SYMBOL_STR(gpiod_get_raw_value) },
	{ 0x1a540a51, __VMLINUX_SYMBOL_STR(gpiod_set_raw_value) },
	{ 0x72528e65, __VMLINUX_SYMBOL_STR(gpio_to_desc) },
	{ 0xb1ad28e0, __VMLINUX_SYMBOL_STR(__gnu_mcount_nc) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "F56AD12D1CDF58CA4D1B6D5");
