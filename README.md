# imagesInMinecraft
Create a mapping from any image file to Minecraft blocks to reproduce the image in Minecraft.
My son and I once spent an afternoon playing with this, it's a little crude and tedious because we have the Xbox version of Minecraft, but I am sure someone could automate it for the PC version.

The basic idea is to map pixels and thier colors, here is the mapping we used:
```
colorNumberings = {'Magenta Wool'   : 1,
                   'Purple Wool'    : 2,
                   'Red Wool'       : 3,
                   'Brown Wool'     : 4,
                   'Orange Wool'    : 5,
                   'Yellow Wool'    : 6,
                   'White Wool'     : 7,
                   'Light Gray Wool': 8,
                   'Gray Wool'      : 9,
                   'Black Wool'     : 10,
                   'Blue Wool'      : 11,
                   'Light Blue Wool': 12,
                   'Cyan Wool'      : 13,
                   'Green Wool'     : 14,
                   'Lime Wool'      : 15,
                   'Pink Wool'      : 16}
```
Then you can input an image file in the \_\_main\_\_ section and get a print out of what each row of Minecraft blocks should be to match the image. To save space, the print out condenses, say, 47 contiguous blocks to be 47x-7. Which means you need to place 47 white wool blocks contiguously. The rows go from 1 being the bottom row to a max row height at the top and blocks are placed as they would be read, from left to right.
