import React, { useState, useEffect } from "react";
import MasonryGrid from "../components/MasonryGrid";
import { getArtPieces } from "../services/api";
import { ArtPiece } from "../types";
import { Button } from "@/components/ui/button";

const HomePage: React.FC = () => {
  const [artPieces, setArtPieces] = useState<ArtPiece[]>([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  const loadMoreArtPieces = async () => {
    setLoading(true);
    try {
      const newArtPieces = await getArtPieces(page);
      setArtPieces((prevArtPieces) => [...prevArtPieces, ...newArtPieces]);
      setPage((prevPage) => prevPage + 1);
    } catch (error) {
      console.error("Error loading art pieces:", error);
    }
    setLoading(false);
  };

  useEffect(() => {
    loadMoreArtPieces();
  }, []);

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Discover Art</h1>
      <MasonryGrid artPieces={artPieces} />
      {!loading && (
        <div className="text-center mt-8">
          <Button onClick={loadMoreArtPieces}>Load More</Button>
        </div>
      )}
    </div>
  );
};

export default HomePage;
