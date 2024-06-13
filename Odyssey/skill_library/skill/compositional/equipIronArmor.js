async function equipIronArmor(bot) {
  // Find the iron_chestplate, iron_leggings, iron_boots, and iron_helmet in the inventory
  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id);
  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id);
  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id);
  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id);

  // Equip the iron_chestplate, iron_leggings, iron_boots, and iron_helmet in the appropriate slots (legs, feet, and head)
  if (ironChestplate) {
    await bot.equip(ironChestplate, "torso");
    bot.chat("Equipped iron chestplate.");
  } else {
    bot.chat("Iron chestplate not found in inventory.");
  }
  if (ironLeggings) {
    await bot.equip(ironLeggings, "legs");
    bot.chat("Equipped iron leggings.");
  } else {
    bot.chat("Iron leggings not found in inventory.");
  }
  if (ironBoots) {
    await bot.equip(ironBoots, "feet");
    bot.chat("Equipped iron boots.");
  } else {
    bot.chat("Iron boots not found in inventory.");
  }
  if (ironHelmet) {
    await bot.equip(ironHelmet, "head");
    bot.chat("Equipped iron helmet.");
  } else {
    bot.chat("Iron helmet not found in inventory.");
  }
}