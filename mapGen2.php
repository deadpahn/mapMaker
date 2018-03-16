<?php
//Map to Blender Version 0.3

if (!isset($argv[1])) {
	die ("Please enter path\n");
	} 

$filePath = $argv[1];
$file = file_get_contents($filePath, true);

$map = new SimpleXMLElement($file);
$mapName = basename($filePath, ".tmx");

define("MAPNAME", $mapName);

$radius = 0.5;
$mapWidth = $map["width"];
$mapHeight = $map["height"];
$arrMap = explode(",", $map->layer->data);

$x = 1 ;
$y = 0 ;
$z = 0 ;

$count = 0;

$blenderFile = "import bpy\n";

foreach ($arrMap as $k) {
	
	if ($count < $mapWidth) {
		$x = $count;
		switch ($k) {
			case "0":
				$command = null;
				//$command = "location=({$x}, {$y}, {$z})";
				break;
			case "1":
			
				$command = "bpy.ops.mesh.primitive_cube_add(radius={$radius}, location=({$x}, {$y}, {$z}))";
				//$command = "location=({$x}, {$y}, {$z})";
				break;
			case "2":
				$command = null;
				break;		
		}
		$count++;
	}
	
	if ($count == ($mapWidth)) {
		$z = $z - 1;
		$count = 0;
		}
	
	if ($command) {
		//print $command ."\n";
		$blenderFile .= $command ."\n";
		$command = null;
		}
}

		$fileBpy = MAPNAME.'.bpy';
		// Write the contents back to the file
		file_put_contents($fileBpy, $blenderFile);

?>
